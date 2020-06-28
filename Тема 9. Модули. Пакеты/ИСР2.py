class Gost_Kniga():
    def __init__(self):
        self.guests = list()


    def add(self, first_name, second_name, age): #добавляем человечка с нужными нам параметрами(имя,фамилия,возраст,страна)
        self.guests.append({"first_namename": first_name,"second_name": second_name, "age": age})
    
    def delete(self, first_name):
        for guests in self.guests:
            if guests.get("guests_age") == age: 
                self.guests.remove(guests) 

    def fail(self): 
        import json
        with open("Гостевая книга.json", 'a') as file:
            json_data = { "Guests": self.guests }
            file.write(json.dumps(json_data, indent=4))
            
if __name__ == "__main__":
    Gost_Kniga = Gost_Kniga()
    Gost_Kniga.add("Ivan", "Ivanov", 16)
    Gost_Kniga.add("Vladimir", "Putin", 18)
    
    Gost_Kniga.fail()