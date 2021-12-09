from class_lib.employee import Employee

e1 = Employee()
e1.set_name("김하늘")
print("사번 : " + str(e1.get_id()) + ", 이름 : " + e1.get_name())

e2 = Employee()
e2.set_name("안산")
print("사번 : " + str(e2.get_id()) + ", 이름 : " + e2.get_name())

e3 = Employee()
e3.set_name("최바다")
print("사번 : " + str(e3.get_id()) + ", 이름 : " + e3.get_name())
