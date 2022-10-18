from mengzi_fine_tuning import MengziZeroShot

mz = MengziZeroShot()
mz.load()

# 使用示例：
# 批量测试
inputs = [  # 实体抽取
    # {
    #     "task_type": "entity_extraction",
    #     "input_string": "导致泗水的砭石受到追捧，价格突然上涨。而泗水县文化市场综合执法局颜鲲表示，根据监控，",
    # },
    # # 语义相似度
    # {
    #     "task_type": "text_similarity",
    #     "input_string": "你好，我还款银行怎么更换",
    #     "input_string_2": "怎么更换绑定还款的卡",
    # },
    # # 金融关系抽取
    # {
    #     "task_type": "financial_relationship_extraction",
    #     "input_string": "为打消市场顾虑,工行两位洋股东——美国运通和安联集团昨晚做出承诺,近期不会减持工行H股。",
    #     "entity1": "工行",
    #     "entity2": "美国运通",
    # },
    # # 广告文案生成
    # {
    #     "task_type": "ad_generation",
    #     "input_string": "类型-裤，版型-宽松，风格-潮，风格-复古，风格-文艺，图案-复古，裤型-直筒裤，裤腰型-高腰，裤口-毛边",
    # },
    # # 医学领域意图分类
    # {"task_type": "medical_domain_intent_classifier", "input_string": "呼气试验阳性什么意思"},
    # # 情感分类
    # {
    #     "task_type": "sentiment_classifier",
    #     "input_string": "房间很一般，小，且让人感觉脏，隔音效果差，能听到走廊的人讲话，走廊光线昏暗，旁边没有什么可吃",
    # },
    # # 评论对象抽取
    # {
    #     "task_type": "comment_object_extraction",
    #     "input_string": "灵水的水质清澈，建议带个浮潜装备，可以看清湖里的小鱼。",
    # },
    # # 新闻分类
    # {"task_type": "news_classifier", "input_string": "懒人适合种的果树：长得多、好打理，果子多得都得送邻居吃"},
    # # 人名抽取
    # {"task_type": "name_extraction", "input_string": "我是张三，我爱北京天安门"},
    # # 公司名抽取
    # {
    #     "task_type": "company_extraction",
    #     "input_string": "就天涯网推出彩票服务频道是否是业内人士所谓的打政策“擦边球”，记者近日对此事求证彩票监管部门。",
    # },
    # 文章摘要
    {
        "task_type": "abstract_gen",
        "input_string": """
居大不易主要是买房子贵啊，生活消费物价大城市比小城市便宜。
我觉得最大的差别就是房租太贵了，如果在南山上班想要通勤时间半小时的，都得 3000 左右的房租了。
就算不买房，租房在普通人的生活成本里也是占大头的，剩下吃穿啥的贵点便宜点根本差不出多少，就住这一项高就足够说成本高了。
只是打工，生活成本当然可以尽量压低。但定居的生活成本就要换一种计算方法了。比如，如果你要在这里发展人际关系，社交成本高不高，如果要在这里找老婆，谈恋爱的金钱支出高不高，结婚生孩子要不要买房，就算不买，租房也不可能太低成本了，一家几口住不能住得太差。
房租太贵，只能在城中村租老旧的房子。想要租好一点的房太难了。
其它全部精简，就说吃住。每月基本 4000 左右。。。
吃啥能花 250 还一周吃几次？
感觉生活好难。
前年来深圳的时候租的 1600 的小单间，没有采光暗无天日。现在租的 2400 的大单间，房间品质还是很恶劣。南山上班，想要 40 分钟内的通勤，一个人住得舒服点，3000 是少不了的。其他物价其实跟二三线城市相比也贵不了多少。。。
跟更小的城市比没概念，但是像楼主说的，一线跟二三线比的话，租房是最大的大头；剩下的包括通勤成本（一线普遍通勤距离更大，尤其是北京，然后仔细观察能发现同样里程一线打车价格比二线贵）；饮食可能稍微贵一些但不明显，主要确实像楼主说的，选择更宽了就可能会去更好的。
来北京海淀工作，保证你有钱花不出去，因为根本没有好吃的…
我以前也认同住在大城市其实各方面比小城市舒服，但租过一次房之后发现，这一项体验的缺失影响太大了。
""",
    },
]


for t in inputs:
    task_type = t["task_type"]
    print(f"task_type:{task_type}")
    input_string = t["input_string"]

    if task_type == "text_similarity":
        input_string_2 = t["input_string_2"]
        res = mz.inference(
            task_type=task_type, input_string=input_string, input_string2=input_string_2
        )
        print(f"input_string1:{input_string}")
        print(f"input_string2:{input_string_2}")
    elif task_type == "financial_relationship_extraction":
        res = mz.inference(
            task_type=task_type,
            input_string=input_string,
            entity1=t["entity1"],
            entity2=t["entity2"],
        )
    else:
        res = mz.inference(task_type=task_type, input_string=input_string)
        print(f"input_string:{input_string}")

    print(f"result:{res}")
    print("————————————————————————————————————————————")
