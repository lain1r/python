#include <Arduino.h>

// структура передаваемых данных
struct Data {
  int32_t num1 = 0;
  int32_t num2 = 0;
};

// данные
Data data;
// указатель на данные
uint8_t *dataP;

void setup() {
  // Говорим что пины в режиме ввода
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);

  // Иницируем подключение по сериал порту
  Serial.begin(9600);

  // Получаем адрес в памяти для переменной data
  dataP = (uint8_t *)&data;
}

void loop() {
  // Читаем значения с пинов и записываем их в структуру
  data.num1 = analogRead(A1);
  data.num2 = analogRead(A2);
  
  // Отправляем байты, что хранятся для структуры Data (первый аргумент - адрес в памяти, второй - кол-во передаваемых байт)
  Serial.write(dataP, sizeof(Data));
  
  // Задержка, чтобы не отправлять слишком много данных
  delay(10);
}