/**
   @version 1.0 2013-12-20
   @author Sergey Botyan
*/

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.TextEvent;
import java.awt.event.TextListener;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.text.MaskFormatter;

//public class DownTime
public class Test
{  
   public static void main(String[] args)
   {  
      CenteredFrame frame = new CenteredFrame();
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setVisible(true);
   }
}

class CenteredFrame extends JFrame
{
	String Result;
   public CenteredFrame()
   {
      // get screen dimensions

      Toolkit kit = Toolkit.getDefaultToolkit();
      Dimension screenSize = kit.getScreenSize();
      int screenHeight = screenSize.height;
      int screenWidth = screenSize.width;

      // center frame in screen

      setSize(370, 100);
      setResizable(false);
      setLocation((screenWidth / 2) - 200, (screenHeight / 2) - 75);

      // set frame icon and title

      Image img = kit.getImage("icon.gif");
      setIconImage(img);
      setTitle("Download Time");
      
      JPanel pnMain = new JPanel();
      pnMain.setLayout(new BoxLayout(pnMain, BoxLayout.X_AXIS));
      pnMain.setBorder(new EmptyBorder(5, 5, 5, 5));
      
      JPanel pnLeft = new JPanel();
      pnLeft.setLayout(new BoxLayout(pnLeft, BoxLayout.Y_AXIS));
      
      JPanel pnRight = new JPanel();
      pnRight.setLayout(new BoxLayout(pnRight, BoxLayout.Y_AXIS));
      //pnRight.setBorder(new EmptyBorder(0, 0, 0, 0));
      
      
      JPanel pnRightUp = new JPanel();
      //pnRightUp.setLayout(new BoxLayout(pnRightUp, BoxLayout.Y_AXIS));
      JPanel pnRightDn = new JPanel();
      //pnRightDn.setLayout(new BoxLayout(pnRightDn, BoxLayout.Y_AXIS));
      // Button
      JButton button = new JButton("Count!");
      button.setPreferredSize(new Dimension(90, 25));
      pnRightUp.add(button);
      // Result Label
      JLabel ResultLabel = new JLabel("Result");
      pnRightDn.add(ResultLabel);
      
      JPanel pnLeftUp = new JPanel();
      pnLeftUp.setLayout(new BoxLayout(pnLeftUp, BoxLayout.X_AXIS));

      JLabel SizeLabel = new JLabel("Enter file size, GB:");
      SizeLabel.setBorder(new EmptyBorder(0, 93, 0, 10));
      pnLeftUp.add(SizeLabel);
      
      Font font = new Font("Calibri", Font.BOLD, 18);
      Insets magin = new Insets(0, 4, 0, 4);
      
      final JTextField Size = new JTextField(){
    	  public void replaceSelection(String content){
    		  super.replaceSelection(content);
    		  String text = getText();
    		  if (text.length() > 4){
    			  setText(text.substring(0, 4));
    			  }
    	    }
      };
      Size.setHorizontalAlignment(JTextField.RIGHT);
      Size.setFont(font);
      Size.setMargin(magin);
      
      // allows only digits & dots
      Size.addKeyListener(new java.awt.event.KeyAdapter() {
          public void keyTyped(java.awt.event.KeyEvent e) {
            char a = e.getKeyChar();
            if (!Character.isDigit(a)
                && (a != '.')
                && (a != '\b')) {
              e.consume();
            }
          }
        });
      
      pnLeftUp.add(Size);
      
      JPanel pnLeftDn = new JPanel();
      pnLeftDn.setLayout(new BoxLayout(pnLeftDn, BoxLayout.X_AXIS));
      
      JLabel SpeedLabel = new JLabel("Enter download speed value, KB/s:");
      SpeedLabel.setBorder(new EmptyBorder(0, 0, 0, 10));
      pnLeftDn.add(SpeedLabel);
      
      final JTextField Speed = new JTextField(){
    	  public void replaceSelection(String content){
    		  super.replaceSelection(content);
    		  String text = getText();
    		  if (text.length() > 4){setText(text.substring(0, 4));}
    	      }
      };
      Speed.setFont(font);
      Speed.setMargin(magin);
      Speed.setHorizontalAlignment(JTextField.RIGHT);
      
      // allows only digits
      Speed.addKeyListener(new java.awt.event.KeyAdapter() {
          public void keyTyped(java.awt.event.KeyEvent e) {
            char a = e.getKeyChar();
            if (!Character.isDigit(a)
                && (a != '\b')) {
              e.consume();
            }
          }
        });
      
      pnLeftDn.add(Speed);
      
      pnMain.add(pnLeft);
      pnMain.add(pnRight);
      pnLeft.add(pnLeftUp);
      pnLeft.add(pnLeftDn);
      pnRight.add(pnRightUp);
      pnRight.add(pnRightDn);
      add(pnMain);
      
      button.addActionListener(new ActionListener(){
    	  public void actionPerformed(ActionEvent ae){
    		  String SizeFieldValue = Size.getText();
    		  double SizeValue = Double.parseDouble(SizeFieldValue);
    		  // GB to KB
    		  SizeValue = SizeValue * 1024 * 1024;
    		  
    		  String SpeedFieldValue = Speed.getText();
    		  int SpeedValue = Integer.parseInt(SpeedFieldValue);
    		  
    		  double ResultSeconds = SizeValue / SpeedValue;
    		  
    		  int ResultHours = (int)(ResultSeconds / 3600);
    		  int ResultMinutes = (int)((ResultSeconds - (ResultHours * 3600)) / 60);
    		  
    		  String Result = (ResultHours + "h " + ResultMinutes + "m");
    		  
    		  System.out.println(Result);
    	  }
      });
      
   }

}