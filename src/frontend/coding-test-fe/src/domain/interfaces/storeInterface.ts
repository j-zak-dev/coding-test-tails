import type { Store } from '../aggregates/Store'

export interface StoreInterface {
    getAll(): Promise<Store[]>
    searchByPostalCode(postalCode: string): Promise<Store[]>
    searchByName(name: string): Promise<Store[]>
}