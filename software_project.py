print("--------WELCOME TO ONLINE VOTING SYSTEM--------\n")
import time
candidate_list=["c1","c2","c3"]
voters_dict={"v1":1,"v2":2,"v3":3,"v4":4,"v5":5,"v6":6,"v7":7,"v8":8,"v9":9,"v10":10}
admin_pass="samyak123"
winner_list = []
def view_voters():
    new_list = []
    for i in voters_dict.keys():
        new_list.append(i)
    print(*new_list)
while(True):
    find_person=int(input("Press: '1'(admin) or '2'(voter) or '3'(exit)\n"))
    if (find_person==1):
        a = input("Enter Password: ")
        if admin_pass==a:
            time.sleep(1)
            print("\nLogin Successfully!\n")
            time.sleep(1)
            while(True):
                b=int(input("Press: '1'(add a candidate) or '2'(remove a candidate) or '3'(add a voter) or '4'(remove a voter) or"
                            " '5'(view candidates) or '6'(view voters) or '7'(exit)\n"))
                if (b==1):
                    candidate_list.append(input("Enter New Name: "))
                    print("Added Successfully!\n")
                elif(b==2):
                    print(*candidate_list)
                    candidate_list.remove(input("Enter Name to remove: "))
                    print("Removed Successfully!\n")
                elif(b==3):
                    sam1=input("Enter New Name: ")
                    voters_dict[sam1]=int(input("Enter a Password: "))
                    print("Added Successfully!\n")
                elif(b==4):
                    view_voters()
                    sam2=input("Enter Name you want to Remove: ")
                    del voters_dict[sam2]
                    print("Removed Successfully!\n")
                elif(b==5):
                    print(*candidate_list,"\n")
                elif (b==6):
                    view_voters()
                    print()
                elif(b==7):
                    print("Exiting from Admin!\n")
                    break
                else:
                    print("Wrong Input!")
                    print("Try Again\n")
        else:
            print("Wrong Password!")
            exit()
    elif(find_person==2):
        while(len(voters_dict)>0):
            view_voters()
            voter_name=input("Choose your Voter ID: ")
            voter_password=int(input("Enter Password: "))
            if (voters_dict[voter_name]==voter_password):
                time.sleep(1)
                print("\nLogin Successfully!\n")
                time.sleep(1)
                print(*candidate_list)
                candidate_choose=input("Choose your Candidate\n")
                winner_list.append(candidate_choose)
                del voters_dict[voter_name]
                print("Voted Successfully!\n")
                time.sleep(1)
                wanna_quit=int(input("Press: '1'(new voter) or '2'(exit)\n"))
                if wanna_quit==2:
                    print("Voting Ends!!!")
                    break
            else:
                print("Wrong Password!\nTry Again\n")
        time.sleep(2)
        print(f"\nTHE WINNER is '{max(winner_list)}' !!!")
        print("\nTHANKS FOR USING!!!")
        exit()
    elif(find_person==3):
        print("\nTHANKS FOR USING!!!")
        break
    else:
        print("Wrong Input!!!\n")
        print("Try Again\n")