#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author: Wei Wu 
@license: Apache Licence 
@file: read_examples.py 
@time: 2019/08/26
@contact: wu.wei@pku.edu.cn

将数据写成可读格式
"""
import random
import os
import json

ROOT = '/data/nfsdata/home/wuwei/182/001-121/'
TRAIN_PERCENT = 0.8
all_labels = {}


def read_ann(fname: str):
    text = open(os.path.join(ROOT, fname + '.txt')).read()
    ann_lines = open(os.path.join(ROOT, fname + '.ann')).readlines()
    anns = ['O'] * len(text)
    for line in ann_lines:
        if line.startswith('R') or 'hard_example' in line:
            continue
        tag, ann, ann_text = line.split('\t')
        tag_name, start, end = ann.split(' ')
        start, end = int(start), int(end)
        assert text[start: end] == ann_text.strip()
        for index in range(start, end):
            if index == start:
                anns[index] = 'B-' + tag_name
            else:
                anns[index] = 'I-' + tag_name
    return text, anns


def convert_to_example(text, anns):
    examples = []

    cur_chars = []
    cur_anns = []
    for i, (c, a) in enumerate(zip(text, anns)):
        cur_chars.append(c)
        cur_anns.append(a)
        if a not in all_labels:
            all_labels[a] = 0
        all_labels[a] += 1
        if i == len(text) -1 or (c == '\n' and text[i + 1] != '\n'):
            if len(cur_chars) > 256:
                cur_chars = cur_chars[:256]
                cur_anns = cur_anns[:256]
                print(cur_chars, cur_anns)
            assert len(cur_chars) == len(cur_anns)
            examples.append({'chars': cur_chars, 'anns': cur_anns})
            cur_chars = []
            cur_anns = []
    return examples


def build_dataset():
    all_examples = []
    for fname in os.listdir(ROOT):
        if fname.endswith('.txt'):
            text, anns = read_ann(fname.replace('.txt', ''))
            all_examples.extend(convert_to_example(text, anns))

    idx = int(len(all_examples) * TRAIN_PERCENT)
    train, test = all_examples[: idx], all_examples[: idx]

    pos_examples = []
    neg_examples = []
    for example in train:
        if set(example['anns']) == {'O'}:
            neg_examples.append(example)
        else:
            pos_examples.append(example)
    print(len(pos_examples), len(neg_examples))
    train = pos_examples + random.sample(neg_examples, 5 * len(pos_examples))

    with open(os.path.join(ROOT, 'train.json'), 'w') as fo:
        for one_train in train:
            fo.write(json.dumps(one_train, ensure_ascii=False) + '\n')

    with open(os.path.join(ROOT, 'test.json'), 'w') as fo:
        for one_test in test:
            fo.write(json.dumps(one_test, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    build_dataset()
    print(all_labels)
