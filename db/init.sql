-- db/init.sql

-- raw_air_quality: One row for every distinct city and timestamp (hour) combination.
-- Note: The raw data is sourced from Open Meteo.
CREATE TABLE raw_air_quality (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    pm2_5 FLOAT,
    pm10 FLOAT,
    ozone FLOAT,
    nitrogen_dioxide FLOAT,
    sulfur_dioxide FLOAT,
    carbon_monoxide FLOAT,
    inserted_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (city, timestamp)
);

-- processed_air_quality: One row for every distinct city and month combination.
CREATE TABLE processed_air_quality (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    pm2_5 FLOAT, -- monthly average of PM2.5 readings
    pm10 FLOAT, -- monthly average of PM10 readings
    ozone FLOAT, -- monthly average of Ozone readings
    nitrogen_dioxide FLOAT, -- monthly average of Nitrogen Dioxide readings
    sulfur_dioxide FLOAT, -- monthly average of Sulfur Dioxide readings
    carbon_monoxide FLOAT, -- monthly average of Carbon Monoxide readings
    hours_available INT NOT NULL, -- how many hourly readings went into this month's average
    processed_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (city, date)
);

-- forecast_air_quality: One row for every distinct city and month combination.
CREATE TABLE forecast_air_quality (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    pm2_5 FLOAT, -- monthly average of PM2.5 readings
    pm10 FLOAT, -- monthly average of PM10 readings
    ozone FLOAT, -- monthly average of Ozone readings
    nitrogen_dioxide FLOAT, -- monthly average of Nitrogen Dioxide readings
    sulfur_dioxide FLOAT, -- monthly average of Sulfur Dioxide readings
    carbon_monoxide FLOAT, -- monthly average of Carbon Monoxide readings
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (city, date)
);

-- pollutant_thresholds: Reference lookup table for UI color coding.
CREATE TABLE pollutant_thresholds (
    id SERIAL PRIMARY KEY,
    pollutant_name VARCHAR(50) NOT NULL UNIQUE,
    middle_limit FLOAT NOT NULL,
    high_limit FLOAT NOT NULL
);

-- Insert default pollutant thresholds for UI color coding.
INSERT INTO pollutant_thresholds (pollutant_name, middle_limit, high_limit) VALUES
('pm2_5', 12.0, 35.4),
('pm10', 54.0, 154.0),
('ozone', 54.0, 70.0),
('nitrogen_dioxide', 53.0, 100.0),
('sulfur_dioxide', 35.0, 75.0),
('carbon_monoxide', 4.4, 9.4)
ON CONFLICT (pollutant_name) DO NOTHING;