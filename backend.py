class Ingredient:
    def __init__(self,Name,Amount,Unit):
        self.Name=Name
        self.Amount=Amount
        self.Unit=Unit

    def __str__(self):
        sep=','
        summary=str(self.Amount)
        summary+=self.Unit+' '
        summary+=self.Name
 

        return summary


#class Recipe:
    #def __init__(self,Name,Ingredients):
        #self.RecipeName=RecipeName
        #self.Ingredients=[]

    #def __str__(self):
        #summary=self.Name+'\n'
        #summary+='{0}'.format(self.Ingredients)

        #return summary

    #def __repr__(self):
        #return self.Ingredients
        
class ShopMateBackend:
    def __init__(self):
        self.Recipes=[]
        self.ShoppingList=[]
        self.Pantry=[]

    def display_recipes(self):
        for x in range(len(self.Recipes)):
            print(self.Recipes[x])
        
    def display_shoppinglist(self):
        for x in range(len(self.ShoppingList)):
            print(self.ShoppingList[x])

    def display_pantry(self):
        for x in range(len(self.Pantry)):
            print(self.Pantry[x])
        
    def save_shopping_list(self,FileName):
        FileObject=open(FileName,"w")
        NumIngredients=len(self.ShoppingList)
        i=0
        while(i<NumIngredients):
            FileObject.write(str(self.ShoppingList[i].Amount)+','+self.ShoppingList[i].Unit+","+self.ShoppingList[i].Name+"\n")
            i+=1
        FileObject.close()
        return i
        
            
    def save_pantry(self,FileName):
        FileObject=open(FileName,"w")
        NumIngredients=len(self.Pantry)
        i=0
        while(i<NumIngredients):
            FileObject.write(str(self.Pantry[i].Amount)+','+self.Pantry[i].Unit+","+self.Pantry[i].Name+"\n")
            i+=1
        FileObject.close()
        return i

    #def load_pantry
    
    #def load_shopping_list

    #def load_recipe

    #def search_recipe

    #def remove_recipe

    def add_ingredient_pantry(self,Name,Amount,Unit):
        self.Pantry.append(Ingredient(Name,Amount,Unit))

    def add_ingredient_shoppinglist(self,Name,Amount,Unit):
        self.ShoppingList.append(Ingredient(Name,Amount,Unit))
    

    def get_matching_ingredients_pantry(self,PartialIngredientName):
        MatchingExpenses=[]
        for e in self.Pantry:
            if PartialIngredientName in e.Name:
                MatchingExpenses.append(e)
            return MatchingExpenses

    def get_matching_ingredients_shoppinglist(self,PartialIngredientName):
        MatchingExpenses=[]
        for e in self.ShoppingList:
            if PartialIngredientName in e.Name:
                MatchingExpenses.append(e)
            return MatchingExpenses
    
    def remove_recipe(self,Recipe):
        self.Recipes.remove(Recipe)

    def add_recipe_shopping_list(self,Recipe,ShoppingList):
        self.ShoppingList.extend(Recipe)

    def clear_shopping_list(self):
        self.ShoppingList.clear()

    def clear_pantry(self):
        self.Pantry.clear()

    def remove_ingredient_shoppinglist(self,Ingredient):
        self.ShoppingList.remove(Ingredient)

    def remove_ingredient_pantry(self,Ingredient):
        self.Pantry.remove(Ingredient)    
    
