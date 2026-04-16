import type { Store } from '../aggregates/Store'

export interface StoreInterface {
    getAll(): Promise<Store[]>
    searchByName(name: string): Promise<Store[]>
    getEnrichedByName(name: string): Promise<Store[]>
}