"NTU_project_map_filled.pkl": is the projected data of NTU map with projection standard "epsg:2062". 

"x_y_bsm.txt": includes 2176 raw location and bsm data

"x_y_bsm_sanitized.txt": includes the corresponding 2176 sanitized bsm data and estimated location data based on the sanitized bsm data

The bsm data in the file includes speed (m/s), heading (rad), accelaration (m/s2)

video: Draw NTU map using the "NTU_map_project_filled.kpl", plot red dot using raw location (in "x_y_bsm.txt" ) and black dot using estimated location (in "x_y_bsm_sanitized.txt" )

The driver behavior is always normal, there are 34 test results with every 64 bsm data.(2176/64=34)