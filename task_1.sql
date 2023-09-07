select login, count("Orders".id)
 	from "Couriers"
 	join "Orders" on "Couriers".id = "Orders"."courierId"
where "inDelivery" = true
group by login;