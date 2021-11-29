package com.company;

public class Main {

    public static void main(String[] args) {
        Catalog vestnik=new Catalog();
        publication j=new Journal("ABC","QWE","CAr","45");
        publication Lama=new Book("Темная башня","Стивен Кинг","Дрофа");
        try {
            vestnik.add(j,0);
            vestnik.get(0).printshow();


        }catch (Exception ex)
        {
            System.out.println(ex.getMessage());
        }

    }
    }




