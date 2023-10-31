def my_var():
    vars = [ 42, 
            "42", 
            "quarante-deux", 
            42.0,
            True,
            [42],
            {42: 42},
            (42,),
            set()
    ]

    for i in vars:
        print(f"{i} has a type {type(i)}")

if __name__ == "__main__":
    my_var()
