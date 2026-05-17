static class Singleton {

    private static Singleton uniqueInstance = null;
    private String value;

    private Singleton() {

    }

    public static Singleton getInstance() {
        if(uniqueInstance == null) {
            synchronized(Singleton.class) {
            uniqueInstance = new Singleton();
            }
        }
        return uniqueInstance;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
