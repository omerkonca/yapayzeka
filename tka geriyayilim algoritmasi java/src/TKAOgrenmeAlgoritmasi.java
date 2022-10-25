import java.util.Random;

public class TKAOgrenmeAlgoritmasi {
    public static void main(String[] args) {
        Random rnd=new Random();
        double[] portakal={1,0};
        double[] elma={0,1};

        double beklenenPortkl=1;
        double beklenenElma=0;

        double w1=1;
        double w2=2;

        double esikDeger=-1.0;
        double ogrenmeKatsayisi=0.5;

        double netPortkl=0;
        double netElma=0;

        int i=0;
        while(netPortkl<esikDeger | netElma>esikDeger){
            System.out.print("Adim  =>  "+i+"  ");
            i+=1;
            netPortkl=portakal[0]*w1+portakal[1]*w2;
            System.out.print("Net Portakal : "+netPortkl+"  ");
            if(netPortkl<esikDeger){
                w1=w1+ogrenmeKatsayisi*portakal[0];
                w2=w2+ogrenmeKatsayisi*portakal[1];
                continue;
            }else{
                netPortkl=beklenenPortkl;
            }
            if(netPortkl==beklenenPortkl){
                netElma=elma[0]*w1+elma[1]*w2;
                System.out.println("Net Elma : "+netElma);
                if(netElma>esikDeger){
                    w1=w1-ogrenmeKatsayisi*elma[0];
                    w2=w2-ogrenmeKatsayisi*elma[1];
                    continue;
                }else{
                    netElma=beklenenElma;
                    break;
                }
            }
        }
        System.out.println("Son Ağırlıklar  : w1 = "+w1+" w2 = "+w2);
        System.out.println("1.Örnek için : NET= w1 : "+w1+" * "+" x1 : "+portakal[0]+" + "+" w2 : "+w2+" * " +" x2 : "+portakal[1]+" = "+netPortkl);
        System.out.println("2.Örnek için : NET= w1 : "+w1+" * "+" x1 : "+elma[0]+" + "+" w2 : "+w2+" * "+" x2 : "+elma[1]+" = "+netElma);



    }
}