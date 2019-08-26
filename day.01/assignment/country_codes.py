def get_country_data(conf):
        iso_country_data = []
        with open('iso_codes.csv', 'r') as country_codes_file:
            for row in country_codes_file.readlines():
                parsed_row = row.split(',')
                country_name = parsed_row[0]  
                iso_code = parsed_row[2]  
                iso_country_data.append({'country_name': country_name, 'iso_code':iso_code})
        iso_country_data.pop(0) # remove header
        return iso_country_data
