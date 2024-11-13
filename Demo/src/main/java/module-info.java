module com.example.sdk {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.sdk to javafx.fxml;
    exports com.example.sdk;
}