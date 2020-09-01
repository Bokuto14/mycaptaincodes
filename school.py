import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:

            writer.writerow(["name", "age" ,"contact number", "E-Mil ID"])

        
        writer.writerow(info_list)
        


if __name__ == '__main__':
    condition=True
    student_num=1

    while(condition):
        student_info=input("Enter some student {}'s information in the following format (Name age contact number E-Mail): ".format(student_num))
        
        
        student_info_list = student_info.split(' ')

        print("\n The entered information is -\nName: {}\nAge : {}\nContact number : {}\n E-Mail: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check= input("Is the entered information correct? (yes/no): ")
        if choice_check=="yes":
             
            write_into_csv(student_info_list)
        
        
            conditional_check=input("enter (yes/no) if you wan to store another student's information")
            if conditional_check=="yes":
                codition=True
                student_num+=1
            elif conditional_check=="no":
                condition=False
                
        elif choice_check=="no":
            print("\nPlease re-enter the value:")
