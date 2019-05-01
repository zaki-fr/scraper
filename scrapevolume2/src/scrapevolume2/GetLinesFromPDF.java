package scrapevolume2;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import org.apache.pdfbox.text.TextPosition;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
/**
* This is an example on how to extract text line by line from pdf document
*/
public class GetLinesFromPDF extends PDFTextStripper {
    
    static List<String> lines = new ArrayList<String>();
    public GetLinesFromPDF() throws IOException {
    }
    /**
     * @throws IOException If there is an error parsing the document.
     */
    public static void main( String[] args ) throws IOException {
    	
        int i =3;
        
    	while(i<=30) {
    	PDDocument document = null;
        PrintWriter writer = new PrintWriter("C:\\Users\\Admin\\Dropbox\\etudes en france\\EPITA\\PRI\\KEA Medicals\\documentation\\cmd"+(i-2)+".txt", "UTF-8");
        String fileName = "C:\\Users\\Admin\\Dropbox\\etudes en france\\EPITA\\PRI\\KEA Medicals\\documentation\\volume2_new_version_Part"+i+".pdf";
        try {
            document = PDDocument.load( new File(fileName) );
            PDFTextStripper stripper = new GetLinesFromPDF();
            stripper.setSortByPosition( false );
            stripper.setStartPage( 0 );
         
           
            stripper.setEndPage( document.getNumberOfPages() );
            Writer dummy = new OutputStreamWriter(new ByteArrayOutputStream());
            stripper.writeText(document, dummy);
            
            // print lines
            for(String line:lines){
            	
            	writer.println(line);
            	
            	
                
            }
        }
        finally {
            if( document != null ) {
                document.close();
            }
        }
        writer.close();
        i++;
    	}
    }
    
}



