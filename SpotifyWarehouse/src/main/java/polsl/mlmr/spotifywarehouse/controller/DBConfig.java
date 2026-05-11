/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package polsl.mlmr.spotifywarehouse.controller;

import jakarta.servlet.ServletContextEvent;
import jakarta.servlet.ServletContextListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Properties;

/**
 *
 * @author milos
 */
public class DBConfig implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent event){
        String url = "jdbc:postgresql://localhost:5432";
        Properties props = new Properties();
        props.setProperty("user", "postgres");
        props.setProperty("password", "m0rg3n");
        // props.setProperty("ssl", "true");
        
        try{
            Connection conn = DriverManager.getConnection(url, props);           
            event.getServletContext().setAttribute("conn", conn);
        }
        catch(Exception e){
            System.out.println("Error setting up the DB:" + e.getMessage());
            e.printStackTrace();
        }
    }
}
