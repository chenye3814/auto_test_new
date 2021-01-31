#coding=utf-8
import time

import random
from config.config import *

import datetime
import random
from config.config import all_list


class parameter_change():

    def __init__(self):
        pass

    @staticmethod
    def get_millisecond_timestamp():
        '''获取毫秒级时间戳'''
        return str(round(time.time() * 1000))

    @staticmethod
    def get_time_stamp():
        '''获取时间戳'''
        return str(round(time.time()))

    @staticmethod
    def get_zdjl_member_id(zdjl_member_id_list):
        '''获取后台我的股池=>指导交流=>群发消息所需入参uids，由member_id构成的字符串'''
        member_id_list = eval(zdjl_member_id_list)
        n = len(member_id_list)
        member_id_str = ''
        for i in range(n):
            member_id_str += member_id_list[i]['member_id']
            if i != n - 1:
                member_id_str += ','
        return member_id_str

    @staticmethod
    def ybwzxq_date_replace(ybwz_date):
        '''研报文章详情字符串拼接'''
        date_list = ybwz_date.split(' ')
        temp_date = date_list[0].split('-')
        return '/' + temp_date[0] + '/' + temp_date[1] + temp_date[2] + '/'

    @staticmethod
    def get_chance_list_len(chance_list_str):
        '''获取机会list的len'''
        if type(chance_list_str) == list:
            return len(chance_list_str)
        else:
            return 0

    @staticmethod
    def str_to_float(temp_str):
        '''字符串转float'''
        return float(temp_str)

    @staticmethod
    def str_to_int(temp_str):
        '''字符串转int'''
        return int(temp_str)

    @staticmethod

    def crm_cookies_set(cookies):
        try:
            cookies = eval(cookies)
            kv_str = ''
            for key in cookies.keys():
                kv_str += key + '=' + cookies[key] + ';'

            return kv_str[:-1]
        except:
            print('error!')

    def get_len(temp):
        """求长度"""
        try:
            temp = eval(temp)
            try:
                return len(temp)
            except:
                return temp
        except:
            return len(temp)

    @staticmethod
    def get_stock_code_msg():
        """从全部股票列表中随机获取一只股票的基本信息"""
        all_stock_list = all_list
        i = random.randint(0,len(all_stock_list)-1)
        # stock_code = temp[i][0]
        stock_code_msg = all_stock_list[i][3]
        # stock_name = temp[i][1]
        return stock_code_msg

    @staticmethod
    def ran_buy_num():
        """人工诊股购买股票股数，随机数"""
        return random.randint(1, 100000000)

    @staticmethod
    def ran_buy_price():
        """人工诊股股票购买价格，保留两位小数，随机数"""
        a = random.uniform(0.01,100000000)
        return round(a,2)

    @staticmethod
    def get_teacher(temp):
        """获取所有可诊股老师并随机返回一个老师id"""
        temp = eval(temp)
        a = random.randint(0,len(temp)-1)
        teacher_id = temp[a]["admin_id"]
        print(222)
        return teacher_id

    @staticmethod
    def get_help_id(temp):
        """获取诊股状态为已完成的诊股报告并随机返回第一个help_id"""
        temp = eval(temp)
        help_id = ""
        for i in temp:
            if i["datastatus"] == "3":
                help_id = i["id"]
                break
        return help_id

    @staticmethod
    def get_st_chance(temp):
        """获取带标的的第一个机会id"""
        temp = eval(temp)
        chance_id = ""
        if len(temp) > 0:
            for i in temp:
                if i["is_stock"] == "1":
                    chance_id = i["chance_id"]
                    break
        return chance_id

    @staticmethod
    def get_nst_chance(temp):
        """获取不带标的的第一个机会id"""
        temp = eval(temp)
        chance_id = ""
        if len(temp) > 0:
            for i in temp:
                if i["is_stock"] == "2":
                    chance_id = i["chance_id"]
                    break
        return chance_id

    @staticmethod
    def get_wb_report_id(temp):
        """获取文本报告的report_id"""
        temp = eval(temp)
        report_id = ""
        if len(temp) > 0:
            for i in temp:
                if i["is_pdf"] == 0:
                    report_id = i["report_id"]
                    break
        return report_id

    @staticmethod
    def get_pdf_report_id(temp):
        """获取文本报告的report_id"""
        temp = eval(temp)
        report_id = ""
        if len(temp) > 0:
            for i in temp:
                if i["is_pdf"] == 1:
                    report_id = i["report_id"]
                    break
        return report_id

    @staticmethod
    def get_user_groupd_id(temp):
        """获取有用户的分组id"""
        temp = eval(temp)
        group_id = ""
        for i in temp:
            if int(i["sales_num"]) > 0:
                group_id = i["group_id"]
                break
        return group_id

    @staticmethod
    def get_qy_groupd_id(temp):
        """获取启用状态的分组id"""
        temp = eval(temp)
        group_id = ""
        for i in temp:
            if int(i["status"]) == 1:
                group_id = i["group_id"]
                break
        return group_id

    @staticmethod
    def get_jy_groupd_id(temp):
        """获取禁用状态的分组id"""
        temp = eval(temp)
        group_id = ""
        for i in temp:
            if int(i["status"]) == 2:
                group_id = i["group_id"]
                break
        return group_id

    @staticmethod
    def get_st_chance_id(temp):
        """机会列表获取带股票的机会id"""
        temp = eval(temp)
        chance_id = ""
        for i in temp:
            if i["is_stock"] == "1":
                chance_id = i["chance_id"]
                break
        return chance_id

    @staticmethod
    def get_nst_chance_id(temp):
        """机会列表获取不带股票的机会id"""
        temp = eval(temp)
        chance_id = ""
        for i in temp:
            if i["is_stock"] == "2":
                chance_id = i["chance_id"]
                break
        return chance_id

    @staticmethod
    def make_cpdt(temp, mode):
        """对股票信息作品基本，组装并添加新增的操盘动态
        mode=add表示新增操盘动态
        mode=alter表示重新编辑已发布的操盘动态"""
        shipping_space = random.randint(1, 8)
        feature = str(time.strftime("%Y-%m-%d--%H:%M:%S",
                                    time.localtime())) + '此时新增的操盘动态公司亮点,此时新增的操盘动态公司亮点,此时新增的操盘动态公司亮点,此时新增的操盘动态公司亮点,此时新增的操盘动态公司亮点'
        skill = str(time.strftime("%Y-%m-%d--%H:%M:%S",
                                  time.localtime())) + '此时新增的操盘动态技术诊断,此时新增的操盘动态技术诊断,此时新增的操盘动态技术诊断,此时新增的操盘动态技术诊断,此时新增的操盘动态技术诊断,'
        reedit_feature = str(
            time.strftime("%Y-%m-%d--%H:%M:%S",
                          time.localtime())) + '重新编辑的公司亮点啊重新编辑的公司亮点啊重新编辑的公司亮点啊重新编辑的公司亮点啊重新编辑的公司亮点啊'
        reedit_skill = str(
            time.strftime("%Y-%m-%d--%H:%M:%S",
                          time.localtime())) + '重新编辑的技术诊断啊重新编辑的技术诊断啊重新编辑的技术诊断啊重新编辑的技术诊断啊重新编辑的技术诊断啊'
        utime = int(time.time())
        temp = eval(temp)
        if mode == 'add':
            del temp[0]['operationDynamic'], temp[0]['macroscopic_title'], temp[0]['macroscopic_content'], temp[0][
                'industry_content']
            temp[0]["dynamic"] = [
                {"shipping_space": shipping_space, "feature": feature, "skill": skill, "utime": utime, "mode": "add",
                 "_status": 2}]
        elif mode == 'alter':
            extra_id = temp[0]['operationDynamic'][0]['extra_id']
            del temp[0]['operationDynamic'], temp[0]['macroscopic_title'], temp[0]['macroscopic_content'], temp[0][
                'industry_content']
            temp[0]["dynamic"] = [
                {"shipping_space": shipping_space, "feature": reedit_feature, "skill": reedit_skill, "utime": utime,
                 "mode": "alter", "_status": 2, "extra_id": extra_id}]
        str_temp = str(temp)
        # str_list = '[' + str_temp + ']'
        str_list = str_temp.replace(' ', '')
        # 需要把单引号转换为双引号，不然接口解析会出错
        str_list = str_list.replace("'", '"')
        return str_list


    @staticmethod
    def chance_title_now():
        """重新编辑机会的标题，加上了时间用于辨别"""
        chance_title_now = str(time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime())) + '机会标题标题'
        return chance_title_now

    @staticmethod
    def promotion_code():
        """随机生成优惠码"""
        a = []
        for i in range(0, 6):
            a.append(str(random.randint(0, 9)))
        promotion_code = ''.join(a)
        return promotion_code

    @staticmethod
    def promotion_time(temp):
        """设置活动开始或结束时间，当前时间往后推多长时间(单位为小时)
        设置结束时间传的时间应该比开始时间长"""
        offset = datetime.timedelta(hours=temp)
        now = datetime.datetime.now()
        return (now+offset).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def promotion_skus(temp):
        """生成提交需要添加的sku，随机取一个进行组装"""
        temp = eval(temp)
        skus = {}
        sku_list = []
        for i in temp:
            if len(i["goods_list"]) > 0 and float(i["goods_list"][0]["sku_list"]["price"]) > 0.01:
                skus["goods_id"] = i["goods_id"]
                skus["goods_name"] = i["goods_name"]
                skus["goods_sku_id"] = i["goods_list"][0]["sku_list"]["goods_sku_id"]
                skus["goods_sku_name"] = i["goods_list"][0]["sku_list"]["sku_list_title"]
                skus["init_price"] = i["goods_list"][0]["sku_list"]["price"]
                skus["init_days"] = i["goods_list"][0]["sku_list"]["init_days"]
                break
        skus["preferential_price"] = str(round(random.uniform(0.01,float(skus["init_price"])),2))
        skus["preferential_days"] = str(random.randint(1,200))
        sku_list.append(skus)
        promotion_skus = str(sku_list).replace("'",'"')
        return promotion_skus

    @staticmethod
    def put_zb_info(zb_info, all_ls, week_or_admins):
        """通过值班信息和所有诊股老师以及传入的需要的信息参数，返回对应的数据
        zb_info = 一周所有的值班信息，list格式
        all_ls = 所有诊股老师信息，list格式
        week_or_admin = 根据传入的参数：返回该日是星期几或者该日有哪些老师们"""
        zb_info = eval(zb_info)
        all_ls = eval(all_ls)
        admins = []
        for i in zb_info:
            if len(i["teachers"]) > 0:
                week = str(i["week"])
                for j in i["teachers"]:
                    admins.append(j["admin_id"])
                break
        for m in all_ls:
            if m["admin_id"] not in admins:
                admins.append(m["admin_id"])
                admins.pop(0)
                admins = ','.join(admins)
                break
        if week_or_admins == "week":
            return week
        elif week_or_admins == "admins":
            return admins

    @staticmethod
    def put_sort(temp):
        """获取当天的排序信息并修改排序值返回"""
        temp = eval(temp)
        for i in temp:
            del i['truename']
            i['sort'] = str(int(i['sort'])+10)
        temp = str(temp)
        temp = temp.replace("'",'"')
        return temp








