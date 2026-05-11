/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package polsl.mlmr.spotifywarehouse.controller;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
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
    
    /**
     * emf is the instance of EntityManagerFactory which will be used by the entire application.
     */
    private EntityManagerFactory emf;
    
    /**
     * em is the instance of the EntityManager which will be used by the entire application.
     */
    private EntityManager em;
    
    @Override
    public void contextInitialized(ServletContextEvent event){       
        
        em = emf.createEntityManager();
        
        try{
            Object version = em.createNativeQuery("SELECT version()").getSingleResult();
            System.out.println(version);
        } finally{
            em.close();
        }
        
        
        // props.setProperty("ssl", "true");
        /*
        try{
            Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/", "postgres", "m0rg3n");           
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
            System.out.println("Meow");
            
        }
        catch(Exception e){
            System.out.println("Error setting up the DB:" + e.getMessage());
            e.printStackTrace();
        }
        */
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
