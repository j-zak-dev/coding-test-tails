export type Store = {
  name: string
  postalCode: string
  coordinates?: {
    latitude: number
    longitude: number
  }
}