import Lab2.bmi as bmi

print("Test_BMI")
def test_bmi_normal_weight():
    height=1.7
    weight=65
    testValue=0
    result = bmi.calculate_bmi(height,weight)
    assert (result==testValue)
def test_bmi_over_weight():
    height = 1.7
    weight = 90
    testValue = 1
    result = bmi.calculate_bmi(height, weight)
    assert (result == testValue)

def test_bmi_under_weight():
    height = 1.7
    weight = 40
    testValue = -1
    result = bmi.calculate_bmi(height, weight)
    assert (result == testValue)
