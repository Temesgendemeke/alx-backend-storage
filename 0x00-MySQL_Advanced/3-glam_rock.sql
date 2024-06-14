--  lists all bands with Glam rock
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan  From metal_bands 
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;