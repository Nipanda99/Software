/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle  nh;

int servo;

void moservo( const std_msgs::Int32 &cuchufli_msg){


  servo=cuchufli_msg.data;
  if (servo==2)
  digitalWrite(LED_BUILTIN, HIGH);   // blink the led
 
  else

  digitalWrite(LED_BUILTIN,LOW);
  
}

ros::Subscriber<std_msgs::Int32> sub("test", &moservo);

void setup()
{ 
  pinMode(LED_BUILTIN, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
