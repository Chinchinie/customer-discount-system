from discount import calculate_discount

def test_vip_customer():
    assert calculate_discount(60000000) == 0.1

def test_normal_customer():
    assert calculate_discount(30000000) == 0

def test_tc03():
    # Tổng trước: 49M
    # Đơn hàng mới: 2M
    # Tổng sau: 51M => theo yêu cầu nghiệp vụ phải được giảm 10%
    assert calculate_discount(49000000) == 0.1