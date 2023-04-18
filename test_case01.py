import pytest
import json
import requests

# 定义一个 fixture，名为 "init"
@pytest.fixture(scope="function")
def init():
    print("\n=== 初始化操作 ===")
    # 执行所有的初始化操作，例如初始化数据库连接、文件读取等
    # 确保在 init fixture 后，所有测试用例均处于相同、独立的环境中
    # ...

    # teardown 方法 用于在每个测试用例执行之后执行销毁操作
    yield
    print("\n=== 操作完成，执行清理工作 ===")
    # 执行所有的销毁操作，例如关闭数据库连接、删除临时文件
    # 确保在 teardown 方法后，所有测试用例均执行完成、并将环境恢复到init 运行之前的状态
    # ...


def test_add():
    # 在测试用例函数参数列表中添加 "init" 参数，pytest 会自动执行 init fixture 方法
    # 模拟需要提交的数据
    body = {
        "startDate": "2023-03-20",
        "endDate": "2023-03-27",
        "tenantId": "9996",
        "requestSwitch": 'true'
    }
    # 将数据转换成json格式
    data = json.dumps(body)

    # 发送post请求
    res = requests.post('https://testdrkhi.drkjk.com/api/global-api/global-platform/internal/tcm/manage/account/get', data=data.encode('utf-8'),
                        headers={'Content-Type': 'application/json',
                                 'x-access-token':'I3txfCdBMiuC8JXVT/2C7RiJKw9Tj+VgY9eyAd5usjoUaFfmmRNmFnvo17qsAXE10FXyjnqAHYOciX2Uu96QBrWbVInkQfVRWjLDkCv23cgdMTFH2JxNJ2LvAfBPx58XmQ32A2FPhPUoLaQwx71373QgT1TueAuve4x953UOWic=,gRgZq2085yAsGpayrK/82/Fq9Km4dqGdVJ8LxFISvDWiMVrrX0TvxxtRKGH88k2xmyCgyoILNi/AuMTYYy75li7cOrkNU6HYfsreviDX2k7Drv6w0EPUGrw1cE9ZLSyQx03PXWDzaki5lB/jWMUe6R4Lsl2xQ0pN8cndcI4jMag=,g6Ve6qAyAW2el08P3LQETclDzKm8BxZl+fFhPHgfr/MYUWldU6jmwuA+cXB/jxtw3wtnR8WgegPBxdCHQQ5vos50t4eVReNZJnBDpPePzdAYfgDtPDJJlGXm44TExOrYHwB2R4lUKHE7QvCDwxrRS04JeHzGfF01S3BEUcSHMuA=,PTdgvPzNpJl/FJwUKYlg27l/KHudWBb6Psd84wypk88rHVxpaXF19ZUGaOxP8JxAPFH1DD2S5XSuGp2vDeV/E5O0CVfr4aB7LFUBE6BtiVTaqXLFvyohJWpwdPzkUmOlC2jTgeQmTjypw1x0faN/DFzDrAwRrqYNkzQYJhvrGec='
                                 })

    # 断言post请求的返回结果
    assert res.status_code == 200
    assert json.loads(res.content)['code'] == 0
