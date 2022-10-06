public class relasi{
        public static void main(String args[]) {
          limas P = new Limas(1.0,2.0,5.0,2.0,2.0,3.0,2.0,7.0);
          P.rumus();
        }
    }
    
    class limas{
        double Sx1; double Sy1; double Sx2; double Sy2; double Px1; double Py1; double Px2; double Py2;
        limas(double Sx1,double Sy1, double Sx2, double Sy2, double Px1, double Py1, double Px2, double Py2){
            this.Sx1 = Sx1;
            this.Sy1 = Sy1;
            this.Sx2 = Sx2;
            this.Sy2 = Sy2;
            this.Px1 = Px1;
            this.Px2 = Px2;
            this.Py1 = Py1;
            this.Py2 = Py2;
        }
        void rumus(){
            double luasSegitiga, luasPersegi, luasLimas;
            System.out.println("=== Data Segitiga ===");
            System.out.println("point\t: " + this.Sx1 + ", " + this.Sy1);
            System.out.println("Sisi Segitiga\t: " + (this.Sy1 + this.Sy2));
            luasSegitiga = 0.5 * (this.Sy1 + this.Sy2) * Math.sqrt(3);
            System.out.println("Luas Segitiga\t: " + luasSegitiga);
            
            
            System.out.println("\n=== Data Persegi ===");
            System.out.println("point\t: " + this.Px1 + ", " + this.Py1);
            System.out.println("Sisi Persegi\t: " + (this.Px1 + this.Px2));
            luasPersegi = (this.Px1 + this.Px2) * (this.Px1 + this.Px2);
            System.out.println("Luas Persegi\t: " + luasPersegi);
            
            luasLimas = (4 * luas_Segitiga) + luasPersegi;
            System.out.println("\n\nLuas Limas : " + luasLimas);
        }
    }
