I created a [new map about tax data in Waltham](https://eamondawes.github.io/landValue.html) and how valuable land is to Waltham from a tax perspective. There are three things that go into the assessed taxes of a property:
1. The value of the property
2. Its land use (residential/commercial)
3. If it is owner-occupied

At the moment (2023) the tax rate is $10.32/$1000 for residential properties and $21.95/$1000 for commercial properties. If a property is owner-occupied, it gets an exception of ~$280k of the total assessed residential value.

When calculating the taxes assesed for each property, I disregard the owner-occupied exception since I'm not confident in the data. I'm also not sure it will make that much of a difference in what it shows (I don't think it will flip a high-paying area to a low-paying one or vice versa). I also assume any mixed use properties have their value split equally between residential and commercial revenue (which is wrong because some mixed used properties are excempt from taxes and some are all commercial) but I don't have the data of how this split occurs so I'm calling those properties $16.13/$1000

If you want to reach out to the Assessors Dept and get me better data, I will actually pay you because they never get back to my emails.

I take each Map Parcel ID, because that is how taxes are assesed, and sum up the ones in the same Location ID. This takes into consideration condos and other buildings with more than one "unit" in the same building. I think I did this right, but I may very well have made a mistake somewhere.

You can view the [raw land value data here](https://github.com/eamondawes/geowaltham/blob/main/data/value_data.json) and will notice that the value per sqft goes from 937 to 0. This is because I multiplied instead of divided when converting from square meters to square feet. Oops, it's fixed in the geojson. Anyway of the 12.7k plots that have tax value, the median is about 96c/sqft. There are only 58 properties with a value between $4.31 and $8.09. This doesn't make a very good linear plot, maybe it doesn't make a good log one either, but I just put it in 10 buckets. You can look at the source to see what's going on there. If a propery pays no taxes it gets grayed out.

The data shows what you would expect, dense neighborhoods provide great value to cities. Even parts of Lakeview are as economical as the South Side. Look at it and explore. I'm always here for questions.
