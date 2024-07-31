class ThreadOne implements Runnable{
    public void run(){
            try {
                for(int i=100; i<=110; i++){
                    System.out.println("Thread 1 - i : "+i);
                     Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            };
        }
    }


    class ThreadTwo implements Runnable{
        public void run(){
                try {
                    for(int i=200; i<=210; i++){
                        System.out.println("Thread 2 - i : "+i);
                         Thread.sleep(1000);
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                };
            }
        }
    
        class ThreadThree implements Runnable{
            public void run(){
                    try {
                        for(int i=300; i<=310; i++){
                            System.out.println("Thread 3 - i : "+i);
                             Thread.sleep(1000);
                        }
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    };
                }
            }

            class ThreadFour implements Runnable{
                public void run(){
                        try {
                            for(int i=400; i<=410; i++){
                                System.out.println("Thread 4 - i : "+i);
                                 Thread.sleep(4000);
                            }
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        };
                    }
                }

class Q1Test0{
    public static void main(String[] args) {
        System.out.println("Main Thread Starts : ");

        ThreadOne one = new ThreadOne();
        Thread t1 = new Thread(one);
        t1.start();
        t1.setPriority(Thread.MIN_PRIORITY);

        ThreadTwo two = new ThreadTwo();
        Thread t2 = new Thread(two);
        t2.start();
        t2.setPriority(Thread.MAX_PRIORITY);

        ThreadThree three = new ThreadThree();
        Thread t3 = new Thread(three);
        t3.start();
        t3.setPriority(Thread.NORM_PRIORITY);

        ThreadFour four = new ThreadFour();
        Thread t4 = new Thread(four);
        t4.start();
        t4.setPriority(Thread.NORM_PRIORITY + 2);
        System.out.println("Main Thread Ends...");

        // t.sleep(3000);



    }
}