#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author: Wei Wu 
@license: Apache Licence 
@file: serve.py 
@time: 2019/08/30
@contact: wu.wei@pku.edu.cn
"""
from bert import Ner
model_path = '/data/nfsdata/home/wuwei/study/BERT-NER/out_event_5'

example = {
    'title': '和平收場光復紅土未現警民衝突',
    'passage': '法国驻华大使:为规避美制裁法德正与伊朗商讨结算机制首单交易原标题:在法国总统提出的15天伊核问题磋商期(7月15日)到期前夕,法国驻华大使黎想近日在接受中国青年报·中国青年网记者采访时透露,法国、德国等国眼下正就帮助伊朗规避美国制裁的易货交易结算机制“贸易往来支持工具”(instex)的运行问题,与伊朗进行 积极沟通,“现在要做的是选定首个可以使用instex进行交易的订单”。黎想向记者表示,法中两国都关注当前的伊朗核问题进展。与中国立场一样,法国也反对美国在伊朗问题上采取的域外管辖等做法,希望能在2015年《联合全面行动计划》(即伊核问题全面协议,以下简称“伊核协议”)框架下解决当前的伊朗问题。他表示:“法国一直致力于维护伊核协议。我们(欧洲三国)从去年开始就在逐步建立可以规避美国域外管辖措施的instex结算机制。”2018年5月,美国宣布退出伊核协议并逐步恢复因协议而中止的对伊制裁,其中就包括对伊朗最为关键的石油出口贸易。为了应对这一问题,欧洲3个伊核协议签署国(英国、法国、德国)于今年1月31日宣布三国将联合建立与伊朗商业结算机制in核在协议中的承诺,如果有'}
model = Ner(model_path)

outputs = model.predict(example['passage'])
outputs = [out for out in outputs if out['tag'] != 'O']
print(outputs)
