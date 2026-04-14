export type Store = {
  name: string
  postalCode: string
}

export type RichStore = {
  name: string
  postalCode: string
  coordinates?: {
    latitude: number
    longitude: number
  }
}