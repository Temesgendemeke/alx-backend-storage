SELECT band_name, COALESCE(split, 2022) - COALESCE(formed, 0) AS lifespan  From holberton.metal_bands 
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;