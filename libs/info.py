infos = [
    {
        'sno': '32106200104',         # 学号
        'pwd': '@Hello0912',         # 密码
        'devName': '307-002',   # 预约的座位号（不足3位数的要补零）
        'name': 'momo',        # 随便起个名字
        'periods': (            # 预约时间段（每段时间不能超过4小时）
            # ('8:30:00', '12:30:00'),
            # ('13:00:00', '17:00:00'),
            # ('17:30:00', '21:30:00')
        ),
        'pushplus': '',         # pushplus 的 token（用于推送消息到微信）
    },

    # 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
  
]
