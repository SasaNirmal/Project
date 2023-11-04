#driver.py
'''
import get_input
import validate
import average
import display

def main():
    num_1,num_2,num_3= get_input.input_data()
    vn1,vn2,vn3 = validate.validate_data(num_1,num_2,num_3)
    avrg = average.find_average(vn1,vn2,vn3)
    display.disp_average(avrg)
    
    
main()


weight=eval(input("Enter the weight :"))
if weight<0:
    print("Invalied Weight")
    
elif 70<=weight<100:
        print("SMALL")

elif 100<=weight<150:
    print("MEDIUM")

elif weight >=150:
    print("LARGE")

else:
    print("REJECTED")
        
'''
list_1=[290,325,404,298,412,417,334,316,318,421,267,290,307,390]

print(F"maxmum distance in travelled :{max(list_1)}")

