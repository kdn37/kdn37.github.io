import sys
import backend

class ShopMateUI:

    def get_str(prompt:str)->str:
        sys.stdout.write(prompt)
        UserStrInput = sys.stdin.readline().strip()
            
        return UserStrInput

    def get_float(prompt:str)->float:

        ProblemWithFloatInput=True
        while(ProblemWithFloatInput):
            sys.stdout.write(prompt)
            try:
                UserFloatInput=float(sys.stdin.readline())
                ProblemWithFloatInput=False
            except ValueError:
                sys.stdout.write(
                    'Value Entered Must be a number\n')
                
        return UserFloatInput

    def get_int(prompt:str)->int:

        ProblemWithIntInput=True
        while(ProblemWithIntInput):
            sys.stdout.write(prompt)
            try:
                UserIntInput=int(sys.stdin.readline())
                ProblemWithIntInput=False
            except ValueError:
                sys.stdout.write(
                    'Value Entered Must be a number\n')
        return UserIntInput

    def search_and_display_matching_ingredient_pantry(self):
        SearchTarget=ShopMateUI.get_str('Enter parital ingredient name\n')
        
        MatchingIngredients=self.Sm_Be_Obj.get_matching_ingredients_pantry(SearchTarget)
        NumMatchingIngredients=len(MatchingIngredients)
        if (NumMatchingIngredients<=0):
            sys.stdout.write('There are no ingredients that matched: '+SearchTarget+'\n')
            return

        sys.stdout.write('\n')

        NamesWidth=20
        AmountsWidth=5
        UnitsWidth=2
        TotalAmount=0
        i=0
        
        ColumnFormat="{:<"+str(NamesWidth)+"}{:<"+str(AmountsWidth)+"}{:>"+str(UnitsWidth)+"}\n"
        RowText=ColumnFormat.format("Name","Amount","Unit")
        sys.stdout.write(RowText)
        
        while(i<NumMatchingIngredients):
            RowText=ColumnFormat.format(MatchingIngredients[i].Name,MatchingIngredients[i].Amount,MatchingIngredients[i].Unit)
            TotalAmount+=MatchingIngredients[i].Amount
            sys.stdout.write(RowText)
            i+=1

        return MatchingIngredients

    def search_and_display_matching_ingredient_shoppinglist(self):
        SearchTarget=ShopMateUI.get_str('Enter parital ingredient name\n')
        
        MatchingIngredients=self.Sm_Be_Obj.get_matching_ingredients_shoppinglist(SearchTarget)
        NumMatchingIngredients=len(MatchingIngredients)
        if (NumMatchingIngredients<=0):
            sys.stdout.write('There are no ingredients that matched: '+SearchTarget+'\n')
            return

        sys.stdout.write('\n')

        NamesWidth=20
        AmountsWidth=5
        UnitsWidth=2
        TotalAmount=0
        i=0
        
        ColumnFormat="{:<"+str(NamesWidth)+"}{:<"+str(AmountsWidth)+"}{:>"+str(UnitsWidth)+"}\n"
        RowText=ColumnFormat.format("Name","Amount","Unit")
        sys.stdout.write(RowText)
        
        while(i<NumMatchingIngredients):
            RowText=ColumnFormat.format(MatchingIngredients[i].Name,MatchingIngredients[i].Amount,MatchingIngredients[i].Unit)
            TotalAmount+=MatchingIngredients[i].Amount
            sys.stdout.write(RowText)
            i+=1

        return MatchingIngredients

    def find_pantry_ingredient_via_menu(self):
        sys.stdout.write("---------------------------\n")
        sys.stdout.write("Find ingredient in pantry--\n")
        sys.stdout.write("---------------------------\n")
        MatchingIngredients=self.search_and_display_matching_ingredient_pantry()

    def find_shoppinglist_ingredient_via_menu(self):
        sys.stdout.write("----------------------------------\n")
        sys.stdout.write("Find ingredient in shopping list--\n")
        sys.stdout.write("----------------------------------\n")
        MatchingIngredients=self.search_and_display_matching_ingredient_shoppinglist()

    def remove_ingredient_in_shoppinglist(self):
        sys.stdout.write("----------------------------------------\n")
        sys.stdout.write("Remove an ingredient from shoppinglist--\n")
        sys.stdout.write("----------------------------------------\n")

        MatchingIngredients=self.search_and_display_matching_ingredient_shoppinglist()

        if (MatchingIngredients==None):
            return

        NumMatchingIngredients= len(MatchingIngredients)
        i=0
        while (i<NumMatchingIngredients):
            self.Sm_Be_Obj.remove_ingredient_shoppinglist(MatchingIngredients[i])
            i+=1

        sys.stdout.write("Above matches were removed.\n")

    def remove_ingredient_in_pantry(self):
        sys.stdout.write("----------------------------------\n")
        sys.stdout.write("Remove an ingredient from pantry--\n")
        sys.stdout.write("----------------------------------\n")

        MatchingIngredients=self.search_and_display_matching_ingredient_pantry()

        if (MatchingIngredients==None):
            return

        NumMatchingIngredients= len(MatchingIngredients)
        i=0
        while (i<NumMatchingIngredients):
            self.Sm_Be_Obj.remove_ingredient_pantry(MatchingIngredients[i])
            i+=1

        sys.stdout.write("Above matches were removed.\n")
        
        
    def __init__(self):
        self.Sm_Be_Obj=backend.ShopMateBackend()
        menu ='Menu\n'
        menu+='[1] Add ingredient to pantry\n'
        menu+='[2] Add ingredient to shopping list\n'
        menu+='[3] Display ingreidents in pantry\n'
        menu+='[4] Display ingredients in shopping list\n'
        menu+='[5] Search ingredient in  pantry\n'
        menu+='[6] Search ingredient in shopping list\n'
        menu+='[7] Clear shopping list\n'
        menu+='[8] Clear pantry inventory\n'
        menu+='[9] Remove ingredient in panty\n'
        menu+='[10] Remove ingredient in shopping list\n'
        menu+='[11] Import recipe *Not in prototype*\n'
        menu+='[12] Search recipe *Not in prototype*\n'
        menu+='[13] Remove Recipe *Not in prototype*\n'
        menu+='[14] Add recipe to shopping list *Not in prototype*\n'
        menu+='[15] Save shopping list\n'
        menu+='[16] Exit\n'
        
        menu+='Choice: \n'

        choice=ShopMateUI.get_int(menu)

        while (choice!='16'):
            #Add ingredient to pantry
            if (choice==1):
                Name=ShopMateUI.get_str('Enter the name of the ingredient\n')
                Amount=ShopMateUI.get_float('Enter the amount of the ingredient\n')
                Unit=ShopMateUI.get_str('Enter the Unit of the ingredient. Can be blank\n')

                self.Sm_Be_Obj.add_ingredient_pantry(Name,Amount,Unit)
            #Add ingredient to shopping list
            elif (choice==2):

                Name=ShopMateUI.get_str('Enter the name of the ingredient\n')
                Amount=ShopMateUI.get_float('Enter the amount of the ingredient\n')
                Unit=ShopMateUI.get_str('Enter the Unit of the ingredient. Can be blank\n')

                self.Sm_Be_Obj.add_ingredient_shoppinglist(Name,Amount,Unit)
            #Displays items in pantry    
            elif (choice==3):
                sys.stdout.write('Items in pantry\n')
                self.Sm_Be_Obj.display_pantry()
                
            #Displays items in shopping list    
            elif (choice==4):
                sys.stdout.write('Items in shopping list\n')
                self.Sm_Be_Obj.display_shoppinglist()

            #Search ingredient in pantry
            elif (choice==5):
                self.find_pantry_ingredient_via_menu()
                
            #Search ingredient in shopping list   
            elif (choice==6):
                self.find_shoppinglist_ingredient_via_menu()
                   
            #clear ingredients in shopping list
            elif (choice==7):
                self.Sm_Be_Obj.clear_shopping_list()
                
            #clear ingredients in pantry
            elif (choice==8):
                self.Sm_Be_Obj.clear_pantry()
                    
            elif (choice==9):
                self.remove_ingredient_in_pantry()
                
            elif (choice==10):
                self.remove_ingredient_in_shoppinglist()

            #elif (choice==11):
                
            #elif (choice==12):

            #elif (choice==13):
                
            #elif (choice==14):

            elif (choice==15):
                FileName= ShopMateUI.get_str(
                'Enter the name of the file you'
                'want to save to.(.csv)\n')
                    
                self.Sm_Be_Obj.save_shopping_list(FileName)

            choice=ShopMateUI.get_int(menu)

            
                
ShopMateUI()
