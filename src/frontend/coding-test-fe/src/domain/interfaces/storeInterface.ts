import type { Store } from '../aggregates/Store'
import type { RichStore } from '../aggregates/Store'

export interface StoreInterface {
    getAll(): Promise<Store[]>
    searchByName(name: string): Promise<Store[]>
    getEnrichedByNames(names: string[]): Promise<RichStore[]>
}