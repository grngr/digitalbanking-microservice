package com.capg.cardservices;

import io.dropwizard.Application;
import io.dropwizard.Configuration;
import io.dropwizard.configuration.ResourceConfigurationSourceProvider;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
 
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.capg.cardservices.dao.CardDAO;
import com.capg.cardservices.model.Card;
import io.dropwizard.db.DataSourceFactory;
import io.dropwizard.hibernate.HibernateBundle;

import com.capg.cardservices.web.CardServicesController;
 
public class App extends Application<CardConfiguration> {
    private static final Logger LOGGER = LoggerFactory.getLogger(App.class);
 
    
    private final HibernateBundle<CardConfiguration> hibernate = new HibernateBundle<CardConfiguration>(Card.class) {
        @Override
        public DataSourceFactory getDataSourceFactory(CardConfiguration configuration) {
            return configuration.getDataSourceFactory();
        }
    };
    
    @Override
    public void initialize(Bootstrap<CardConfiguration> b) {
    	
    	b.addBundle(hibernate);
    	b.setConfigurationSourceProvider(
                new ResourceConfigurationSourceProvider());

    }
    @Override
    public void run(CardConfiguration c, Environment e) throws Exception {
        LOGGER.info("Registering REST resources");
         final CardDAO dao = new CardDAO(hibernate.getSessionFactory());
        e.jersey().register(new CardServicesController(dao));
    }
 
    public static void main(String[] args) throws Exception {
        new App().run(args);
    }
}