import java.io.File;
public class file_scaner {
    public static void main( String [] args ) {
        File actual = new File(".");
        for( File f : actual.listFiles()){
            System.out.println( f.getName() );
        }
    }
}