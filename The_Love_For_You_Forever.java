/*
 * I love three things in this world
 * Sun, Moon and You
 * Sun for morning, Moon for night, and You
 * forever
 *
 * 浮世三千，吾爱有三
 * 日，月与卿
 * 日为朝，月为暮
 * 卿为朝朝暮暮
 * */

public class The_Love_For_You_Forever {

    static class Three_Things_I_Loved {

        final String First_Thing = "You";
        final String Second_Thing = "Sun";
        final String Third_Thing = "Moon";

        public String Confession() {

            return "I love " + First_Thing + " forever. Never forget, never give up!";
        }
    }

    public static void main(String[] args) {
        Three_Things_I_Loved MyLove = new Three_Things_I_Loved();
        System.out.println(MyLove.Confession());
    }
}