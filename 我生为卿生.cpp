/*
   我生为卿生，卿生赴我媒，同心两相知，长命无绝衰
*/

//人
class Person{
//...
private:
  void* id;    //本我
  void* ego;    //自我
  void* superego;  //超我
};

//伴侣——不分你我地联合
union Couple{
  void* you;
  void* me;
};

//生生世世的伴侣们
vector<Couple*>* timelessCouples = new vector<Couple*>();
  
//有你、有我的世界  
int main(int argc, char** argv){
  //亘古...
  
  timeFlies();//...岁月...
  
  Person* me = new Person();//我
  
  timeFlies();//...岁月...

  Person* you = new Person();//你
  
  timeFlies();//...岁月...

  if(check(time, place, you, me) == true){
    //如果时间、地点，还有你，都没有异见，我愿陪你，从亘古到永远
    Couple * newCouple = new Couple();
    newCouple->me = you;
    timelessCouples->push_back(newCouple);
  }
  
  timeFlies();//...岁月...
  
  //永远...  
  
  return 0;
}