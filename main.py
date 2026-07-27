# lucky_number=[4,8,15,16]
# freinds=["kevin","Karen","jim"]
# freinds.reverse()
# print(freinds)

# def sayHi():
#     print('Hello Bruce')
# sayHi()
# is_male=False
# is_Tall=True

# if is_male or is_Tall :
#     print("you are the male")
# elif is_male and is_Tall:
#     print("You are cover boy")
# else:
#     print("you are the female")


# def max_num(num1,num2,num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3

# print(max_num(2,3,4))

# freinds=['Mucyo',"bruce"]
# for freind in freinds:
#     print(freind)
# 
# student = {
#     "name": "Bruce",
#     "age": 21,
#     "country": "Rwanda"
# }
# for key in student:
#     print(key)

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def login(self):
        print(self.name,"logged in")

user1=User("bruce","bruceEmail@gmail.com")
print(user1.name)
user1.login()