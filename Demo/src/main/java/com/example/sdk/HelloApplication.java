package com.example.sdk;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.io.FileInputStream;
import java.io.IOException;
import java.security.cert.PolicyNode;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        //FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Group root=new Group();
        Group root2=new Group();

        Scene scene1 = new Scene(root, Color.AQUA);


        stage.setWidth(700);
        stage.setHeight(600);

        stage.setTitle("JavaFx Classs 2");
        stage.setScene(scene1);

        //for text
        Text txt=new Text();
        txt.setText("Varsity te 11.11 chole");
        txt.setX(100);
        txt.setY(150);
        txt.setFont(Font.font("Impact",25));
        txt.setFill(Color.valueOf("#277b10"));
        root.getChildren().add(txt);

        //Button
        Button  btn=new Button();
        btn.setText("Understandable");
        btn.setLayoutX(250);
        btn.setLayoutY(250);
        //btn.setPrefSize(Font.font("Impact",15));
        root.getChildren().add(btn);


        //Circlr
        //Circlr circ=new Circle();
       // circ.setCenterX(300);
        //circ.setCenterY(325);
       // circ.setRadious(40);


        //Add Icon
        Image icon=new Image(new FileInputStream("C:\\Users\\student\\Desktop\\Javafx folder\\sdk\\src\\icon.png"));
         stage.getIcons().add(icon);

        //next button


        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}