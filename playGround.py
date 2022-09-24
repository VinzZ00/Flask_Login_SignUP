from Account import Account as acc

print(__name__);

def one() :
    x:str = "elvin12"

    if x :
        print("ini berisi");
        print(f"isi nya adalah \"{x}\"")
        print(x.isalnum())
    if x == None : 
        print("Ini Null");
    x = acc("Elvin", "12-02-2002", "elvin.sestomi@binus.ac.id", password= "Elvin123");

    print(type(x));

    y, booly = x.getName();

    print(booly);
    
    pass

def two() :

    def OuterOuterFunc(Name:str) :
        def outerFunc(Func) :
            def innerFunc() :
                print("ini dari inner")
                Func()
            return innerFunc
        print("ini inner kedua")
        print(f"Nama mu adalah {Name}")
        return outerFunc
    
    @OuterOuterFunc("Elvin")
    def decorate() :
        print('Ini dari decorator');

    

    # @decorate
    # def Decorate2() :
    #     print("ini dari decorator ke2");

    decorate()

if __name__ == "__main__" :
    two();
    pass






