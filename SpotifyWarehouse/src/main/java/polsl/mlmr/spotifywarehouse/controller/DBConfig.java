/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package polsl.mlmr.spotifywarehouse.controller;

import jakarta.servlet.ServletContextEvent;
import jakarta.servlet.ServletContextListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.util.Properties;

/**
 *
 * @author milos
 */
public class DBConfig implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent event){
        String url = "jdbc:postgresql://localhost:5432/postgres";
        Properties props = new Properties();
        props.setProperty("user", "postgres");
        props.setProperty("password", "m0rg3n");
        // props.setProperty("ssl", "true");
        
        try{
            Connection conn = DriverManager.getConnection(url, props);           
            event.getServletContext().setAttribute("conn", conn);
            System.out.println("Connection established");
            
            String testTable = "IF NOT EXISTS CREATE TABLE test ("
                    + "test_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                    + "name VARCHAR(50)"
                    + ");";
            //PreparedStatement ps = conn.prepareStatement(testTable);
            Statement st = conn.createStatement();
            
            st.execute(testTable);
            
            st.close();
            
        }
        catch(Exception e){
            System.out.println("Error setting up the DB:" + e.getMessage());
            e.printStackTrace();
        }
    }
    
    @Override
    public void contextDestroyed(ServletContextEvent event){
        try{
            Connection conn = (Connection) event.getServletContext().getAttribute("conn");
            if(conn != null)
                conn.close();
        }
        catch (Exception e){
            System.out.println("Proble with closing db connection: " + e.getMessage());
        }
    }
}
