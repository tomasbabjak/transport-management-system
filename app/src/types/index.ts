export interface Waypoint {
    id?: number
    location: string
    waypoint_type: 'Pickup' | 'Delivery'
}
  
export interface TransportOrder {
    id?: number
    order_number: string
    customer_name: string
    date: string
    waypoints: Waypoint[] | []
}