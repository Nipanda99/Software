/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */
  
#include <Servo.h>
#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle  nh;

Servo myservo;
int luz;
int servo2;
//myservo.attach(9);  // vincula el servo al pin digital 9

void lux( const std_msgs::Int32 &cuchufli_msg){


  luz=cuchufli_msg.data;
  if (luz==2)
  digitalWrite(LED_BUILTIN, HIGH);   // blink the led
 
  else

  digitalWrite(LED_BUILTIN,LOW);
  
}

ros::Subscriber<std_msgs::Int32> sub("test", &lux);

void movmotor( const std_msgs::Int32 &cuchufli2_msg){
  


            int motor=cuchufli2_msg.data;
              if (motor==4){
            int motorPin = 3;
           digitalWrite(motorPin, HIGH);
}
}

ros::Subscriber<std_msgs::Int32> sub2("toserv3", &movmotor);

void movservo2( const std_msgs::Int32 &cuchufli2_msg){


                    servo2=cuchufli2_msg.data;
                    if (servo2==3){
                   // crea el objeto servo
                 
                int pos = 0;    // posicion del servo
                    {
                   //varia la posicion de 0 a 180, con esperas de 15ms
                   for (int pos = 0; pos <= 180; pos += 1) 
                   {
                      myservo.write(pos);              
                      delay(15);                       
                   }
                 
                   //varia la posicion de 0 a 180, con esperas de 15ms
                   for (int pos = 180; pos >= 0; pos -= 1) {
                      myservo.write(pos);              
                      delay(15);                       
                   }

}
}
}

ros::Subscriber<std_msgs::Int32> sub1("toserv2", &movservo2);



void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  nh.subscribe(sub1);
  nh.subscribe(sub2);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
