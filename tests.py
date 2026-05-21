pruebas = [
    """
    int x = 5;
    float y = 3.14;

    if(x > 0){
        x = x - 1;
    }
    else{
        x=0;
    }
    """,

    """
    int suma(int a, int b){
        int r;
        r = a + b;
        return r;
    }

    int main(){
        int total;
        total = suma(3, 4);

        print(total);

        return total;
    }
    """,
    """
    int x = 1;

    while(x <= 5){
        x = x + 1;

        if(x != 3){
            print("hola");
        }else{
            print("chau");
        }
    }

    return x;
    """,
    """
    bool flag = true;

    if(flag && true){
        print("ok");
    }
    """,
    """
    void saludo(){
        print("hola");
        return;
    }

    int main(){
        saludo();
        return 0;
    }
    """,
    """
    int x = 0;

    for(x = 0; x < 5; x = x + 1){
        print(x);
    }
    """,
    """
    int x;

    read(x);

    if(!(x == 0)){
        print(x);
    }
    """,
    """
    int calc(){
        int y;
        y = (5 + 3) * 2 / 4;
        return y;
    }
    """,
    """
    float n = -3.5;

    if(n >= 0 || n < 10){
        print(n);
    }
    """,
]
#Nota: estas pruebas deben cubrir el uso de todos los tokens, así como también casos de error

pruebaserror = [
#los que dan error
    """
    int x = 5 @ 3;
    """,
]