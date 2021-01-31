from public.interface.process_class import process_class
from public.interface.excel_database_exchange import to_database
from public.common.common import modify_hosts
from config.config import hosts


def main():
    # modify_hosts(hosts['CXTyf'])
    a = process_class()
    # a.set_test_process(['内容管理=>新增机会','内容管理=>操盘动态','内容管理=>标的出局']) #list内使用单引号隔开，不要使用双引号
    a.set_test_process(['人工诊股'])
    # a.set_test_project("股先生APP")

    # a.set_test_task("行情接口")
    dict_set = {"appcode": "5ca4baf2937f40jyu4z42862"}
    a.set_global_dict(dict_set)

    # a.set_test_task("行情接口2")
    # 内网、预发环境相关账号设置
    yfb_env_set = {"appcode": "5ca4baf2937f40jyu4z42862",
                   "psw": "123456Aa",
                   "zgls_acc": "chenye01",
                   "super_admin": "DXGS8888",
                   "new_bd": "xinjian",
                   "bd_yisheng": "yisheng",
                   "bd_ersheng": "ersheng",
                   "neirong": "neirong"}

    inner_env_set = {"appcode": "5c3d73a0f1f18c30cqb5zkov",
                     "psw": "123456Aa",
                     "zgls_acc": "chenye01",
                     "super_admin": "DXFGS001",
                     "new_bd": "newbiaodi",
                     "bd_yisheng": "oneshen",
                     "bd_ersheng": "twoshen",
                     "neirong": "chenye02"}

    # a.set_global_dict(inner_env_set)

    a.run()
    print("开干")


if __name__ == '__main__':
    # to_database(r"./excel_file/dx_interface_app.xls")

    # to_database(r"C:\Users\admin\Desktop\dx_interface_cloud.xls")

    main()
