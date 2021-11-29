package com.company;

public class Catalog {

        private final int size = 16;
        private final int rate = 4;
        private publication[] array = new publication[size];
        private int pointer = 0;


        public void add(publication item)throws ArrayIndexOutOfBoundsException {
            if (pointer == array.length - 1) throw new ArrayIndexOutOfBoundsException("Элемента не существует");
            resize(array.length * 2); // увеличу в 2 раза, если достигли границ
            array[pointer++] = item;
        }

        public void add(publication _object, int number)throws ArrayIndexOutOfBoundsException {
            if (number > pointer) throw new ArrayIndexOutOfBoundsException(number);
            pointer++;
            if (number == 0) {
                array[0] = _object;
            } else {

                for (int i = size - 1; i < number; i--) {
                    array[i] = array[i - 1];
                }
                array[number + 1] = _object;
            }
        }


        public publication get(int index) throws ArrayIndexOutOfBoundsException
        {
            if (index>pointer) throw new ArrayIndexOutOfBoundsException();
            return array[index];
        }


        public void remove(int index)throws Exception {
            for (int i = index; i < pointer; i++)
                array[i] = array[i + 1];
            array[pointer] = null;
            pointer--;
            if (array.length > size && pointer < array.length / rate)
                throw new ArrayIndexOutOfBoundsException("Элемента не существует");
            resize(array.length / 2); // если элементов в CUT_RATE раз меньше чем
            // длина массива, то уменьшу в два раза
        }


        public int size() {
            return pointer;
        }


        private void resize(int newLength) {
            publication[] newArray = new publication[newLength];
            System.arraycopy(array, 0, newArray, 0, pointer);
            array = newArray;
        }
    }

