
-- Author:              A. Ireland
--
-- Address:             School Mathematical & Computer Sciences
--                      Heriot-Watt University
--                      Edinburgh, EH14 4AS
--
-- E-mail:              a.ireland@hw.ac.uk
--
-- Last modified:       13/10/2002
--
-- Filename:            env.ads
--
-- Description:         Provides the drivers required for simulating the
--                      environment in which the ATP system operates.

package Env is

  subtype Sensor_Range is Integer range 0..3;

  procedure Update;

  function At_End return Boolean;

  procedure Open_File;

  procedure Close_File;

end Env;



